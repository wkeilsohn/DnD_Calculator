function PageNumber(){
	var num = Math.floor((Math.random() * 30) + 1);
	num = Math.floor(num / 10);
	return(num);
}


function NumString(){
	num = PageNumber();
	num = num.toString();
	num = "/static/images/pic".concat(num, ".jpg");
	num = decodeURIComponent("url('".concat(num, "')"));
	return(num);
}