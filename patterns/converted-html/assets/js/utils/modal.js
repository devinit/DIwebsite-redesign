import $ from 'jquery';

// export default function accordion (trigger, triggerActive, target, targetActive) {
//     $(trigger).on('click', function(e) {
// 		e.preventDefault();
// 		$(this).toggleClass(triggerActive);
// 		$(this).next(target).toggleClass(targetActive);
// 	});
// }



export default function modal (target, trigger, parentcontainer) {

	var modal			= document.getElementById(target),
		body			= document.getElementsByTagName("body"),
		container		= document.getElementById(parentcontainer),
		button_close	= document.getElementById("modal-button-close");

	$(trigger).on('click', function(event) {
		event.preventDefault();
		/* Act on the event */
		modal.className="modal is-visually-hidden",
			setTimeout(function(){
				container.className="modal-container is-blurred",
				modal.className="modal"
			},
		100),
		container.parentElement.className="modal-open"
	});

	button_close.onclick=function(){
		modal.className="modal is-hidden is-visually-hidden",
		body.className="",
		container.className="modal-container",
		container.parentElement.className=""
	}

	window.onclick=function(e){
		e.target==modal&&(
			modal.className="modal is-hidden",
			body.className="",
			container.className="modal-container",
			container.parentElement.className=""
		)
	}
}