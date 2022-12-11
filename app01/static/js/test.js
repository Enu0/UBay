$(function () {       
    $("#focusNews").KinSlideshow({
   //   moveStyle:"down", 		//设置切换方向为向下 [默认向左切换]
      intervalTime:8,   		//设置间隔时间为8秒  [默认为5秒]
      mouseEvent:"mouseover",		//设置鼠标事件为“鼠标滑过切换”  [默认鼠标点击时切换]
      titleFont:{TitleFont_size:14,TitleFont_color:"#FF0000"} //设置标题文字大小为14px，颜色：#FF0000
  });
 
})