import $ from 'jquery';

export default function setupNotices(
  selector = '[data-notice]',
  trigger_all = '[data-notice-accept-all]',
  trigger_necessary = '[data-notice-accept-necessary]'
) {

  $(trigger_all).on('click', e => {
    e.preventDefault();
    const notice = $(e.target).closest(selector).first();
    dismissNotice(e.target, notice, "all");
  });

  $(trigger_necessary).on('click', e => {
    e.preventDefault();
    const notice = $(e.target).closest(selector).first();
    dismissNotice(e.target, notice, "necessary");
  });

  function uuidv4() {
    return "10000000-1000-4000-8000-100000000000".replace(/[018]/g, c =>
      (+c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> +c / 4).toString(16)
    );
  }

  function getCookie(key) {
    var keyValue = document.cookie.match('(^|;) ?' + key + '=([^;]*)(;|$)');
    return keyValue ? keyValue[2] : null;
  }

  function dismissNotice(trigger, notice, choice) {
    const id = trigger.id;
    let token = getCookie(id + '_token');
    if(token === null){
      token = uuidv4();
    }
    const csrf_token = getCookie('csrftoken');
    setCookie(id, 'dismissed');
    setCookie(id + '_choice', choice);
    setCookie(id + '_token', token);
    if(choice == "necessary"){
      $(trigger_all).removeClass('button--radioactive');
    }else{
      $(trigger_necessary).removeClass('button--radioactive');
    }
    $(trigger).addClass('button--radioactive');
    notice.slideUp(300, ()=> {
      notice.remove();
    });
    const log_obj = {
      'token': token,
      'url': $(location).prop('href'),
      'user_agent': navigator.userAgent,
      'choice': choice
    };
    $.ajax({
      url: '/api/cookie-consent/',
      type: 'POST',
      headers:{
        "X-CSRFToken": csrf_token
      },
      contentType: 'application/json; charset=utf-8',
      data: JSON.stringify(log_obj),
      dataType: 'json'
    });
  }


  function setCookie(key, value) {
      var today = new Date();
      var expire = new Date();
      expire.setTime(today.getTime() + 3600000 * 24 * 30 * 6);
      document.cookie = key + "=" + encodeURI(value) + ";expires=" + expire.toGMTString() + ';path=/';
  }
};
