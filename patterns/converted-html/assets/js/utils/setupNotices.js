import $ from 'jquery';

export default function setupNotices(
	selector = '[data-notice]',
	trigger = '[data-notice-accept]'
) {

	$(trigger).on('click', e => {
		e.preventDefault();
    const choice = e.target.id;
		const notice = $(e.target).closest(selector).first();
		if (notice) {
			dismissNotice(notice, choice);
		}
	});

	function dismissNotice(notice, choice) {
		const id = notice.attr('id');
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
