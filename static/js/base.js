/*global bootstrap:false*/
/*jshint esversion:6*/

let toastElList = [].slice.call(document.querySelectorAll('.toast'));
toastElList.map(function (toastEl) {
let option = {
    animation: true,
    autohide: true,
    delay: 5000,
};
let bsToast = new bootstrap.Toast(toastEl, option);
bsToast.show();
});
