(()=>{var e=function(){function e(e,t){this.html=e,this.idPattern=t}return e.prototype.render=function(e,t,r,a){var i=this.html.replace(/__NAME__/g,t).replace(/__ID__/g,r);e.outerHTML=i;var n=createImageChooser(r);return n.setState(a),n},e}();window.telepath.register("wagtail.images.widgets.ImageChooser",e)})();