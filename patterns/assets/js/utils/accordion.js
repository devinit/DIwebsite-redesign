import $ from 'jquery';

export default function accordion (trigger, triggerActive, target, targetActive) {
    $(trigger).on('click', function(e) {
		e.preventDefault();
		$(this).toggleClass(triggerActive);
		$(this).next(target).toggleClass(targetActive);
	});
}
