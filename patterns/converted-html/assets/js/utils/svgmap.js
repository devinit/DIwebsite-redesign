export default function initSVGmap () {
    var world = document.getElementById("world");
    world.addEventListener("load", function () {
        var doc = world.getSVGDocument();
        doc.querySelector("[cc=us]").style.fill = "red";
        doc.querySelector("[cc=gb]").style.fill = "red";
        doc.querySelector("[cc=ug]").style.fill = "red";
        doc.querySelector("[cc=ke]").style.fill = "red";
    });
}