import $ from 'jquery';

export default function setupNotices(
	selector = '[data-notice]',
	trigger_all = '[data-notice-accept-all]',
  trigger_necessary = '[data-notice-accept-necessary]'
) {

	$(trigger_all).on('click', e => {
		e.preventDefault();
		const notice = $(e.target).closest(selector).first();
		if (notice) {
			dismissNotice(e.target, notice, "all");
		}
	});

  $(trigger_necessary).on('click', e => {
		e.preventDefault();
		const notice = $(e.target).closest(selector).first();
		if (notice) {
			dismissNotice(e.target, notice, "necessary");
		}
	});

	function dismissNotice(trigger, notice, choice) {
		const id = trigger.id;
		setCookie(id, 'dismissed');
    setCookie(id + '-choice', choice);
		notice.slideUp(300, ()=> {
			notice.remove();
		});
	}

	function setCookie(key, value) {
	    var today = new Date();
	    var expire = new Date();
	    expire.setTime(today.getTime() + 3600000 * 24 * 14);
	    document.cookie = key + "=" + encodeURI(value) + ";expires=" + expire.toGMTString() + ';path=/';
	}
};
