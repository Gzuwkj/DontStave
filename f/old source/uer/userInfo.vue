<template>
  <div class="w-100" id="userInfo">
    <div class="w-100 top-ImageBackground-box position-relative">
      <div class="w-100 position-absolute d-flex justify-content-center align-items-center bg-white">
        <div class="container cur-UserImage d-flex align-items-center">
          <div class="UserImage bg-white d-flex justify-content-center align-items-center">
            <img src="/static/image/default.jpg" alt="">
          </div>
          <div class="position-absolute UserImage-up" @click="openModal">
            <svg viewBox="0 0 1024 1024" width="25" height="25">
              <path fill="currentColor" d="M825.6 448a37.12 37.12 0 0 0-37.12 37.76v243.2a56.96 56.96 0 0 1-56.32 56.32H291.84a56.96 56.96 0 0 1-56.32-56.32v-441.6a56.96 56.96 0 0 1 56.32-56.32h248.32A37.12 37.12 0 0 0 576 192a33.28 33.28 0 0 0-37.12-32.64H291.84a128 128 0 0 0-128 128v439.68a128 128 0 0 0 128 128h439.68a128 128 0 0 0 128-128V488.32c-1.28-23.04-15.36-40.32-33.92-40.32z" />
              <path fill="currentColor" d="M362.24 647.68a33.92 33.92 0 0 0 46.72 0l412.16-412.16a36.48 36.48 0 1 0-51.2-51.2L362.24 600.96a42.24 42.24 0 0 0 0 46.72z" />
            </svg>
          </div>
          <div class="mid-content-box col-md-6 col-8 d-flex flex-column px-3 py-1 justify-content-between">
            <h5 class="mb-1">{{userInfo.username}}</h5>
            <div class="position-relative">
              <input type="text" class="UserDs px-2" :placeholder='userInfo.description'>
              <button class="UserDs-submit-btn position-absolute">发送</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container px-0">
      <div class="w-100 pt-2 row px-4 justify-content-between">
        <aside class="bg-white user-info-card px-3">
          <div class="row px-3 my-3 py-0 justify-content-between align-items-center">
            <h5 class="my-0">基本信息:</h5>
            <div>
              <button v-show="user_info_editor" @click="user_info_editor=false" class="btn btn-secondary btn-sm">取消</button>
              <button @click="user_info_editor=true" class="btn btn-success btn-sm">{{user_info_editor ? "保存" : "编辑"}}</button>
            </div>
          </div>
          <hr class="mx-0 my-2">
          <ul class="px-1">
            <li>
              昵称:
              <div class="ml-3 px-0 input-group input-group-sm col-8">
                <span v-show="!user_info_editor">{{userInfo.nickname}}</span>
                <input v-show="user_info_editor" type="text"  class="form-control" :placeholder="userInfo.nickname">
              </div>
            </li>
            <li>
              学校:
              <div class="ml-3 px-0 input-group input-group-sm col-8">
                <span v-show="!user_info_editor">{{userInfo.school}}</span>
                <input v-show="user_info_editor" type="text"  class="form-control" :placeholder="userInfo.school">
              </div>
            </li>
            <li>
              专业:
              <div class="ml-3 px-0 input-group input-group-sm col-8">
                <span v-show="!user_info_editor">{{userInfo.major}}</span>
                <input v-show="user_info_editor" type="text"  class="form-control" :placeholder="userInfo.major">
              </div>
            </li>
          </ul>
        </aside>
        <div class="bg-white user-dynamic ml-2 px-3 pt-3">
          <div>
            <line-example></line-example>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade">
      <div class="modal-dialog ">
        <div class="modal-content bg-light">
          <div class="modal-header">
            <h5 class="modal-title">头像修改</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body d-flex flex-column align-items-center justify-content-between">
            <div id="myca" class="position-relative ">
              <canvas height="600" width="600"/>
            </div>
            <div class="select-head-image mb-4 position-relative shadow">
              <img id="previewImg" draggable="false" :src="changeHeadImage.file" alt="">
              <div draggable="false" @mousedown="setSelectPosition($event)"></div>
            </div>
            <div class="slider-block">
              <input @input="setSelectSize($event)" id="resize" type="range" min="0" max="500" value="500">
            </div>
          </div>
          <div class="modal-footer position-relative">
            <button @click="$refs.fileChooser.click()" type="button" class="btn btn-success position-absolute" style="left: .75rem">选择图片</button>
            <input ref="fileChooser" @change="selectHeadImage($event)" type="file" class="invisible" value="选择图片">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary">确认修改</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import LineExample from './userInfo_lineChart'
  export default {
    name: "userInfo",
    data(){
      return {
        userInfo: {
          username: 'Gzuwkj',
          description: '早日超脱！！！',
          nickname: '文坤建',
          rating: 1500,
          school: '贵州大学',
          major: '信息安全',
        },
        user_info_editor: false,
        changeHeadImage: {
          file: '', /* 图片内容 */
          maxWidth: 0, /*图片展示最大宽度*/
          maxHeight: 0,/*图片展示最大高度*/
          maxSize: 0,/*选择框最大高度*/
          naturalWidth: 0,/*图片原始宽度*/
          naturalHeight: 0,/*图片原始高度*/
          offsetLeft: 0,/*图片左边相对父元素位置*/
          offsetWidth: 0,/*图片宽度*/
          offsetTop: 0,/*图片上边相对父元素位置*/
          offsetHeight: 0,/*图片高度*/
          select: '',/*选择框jq对象*/
          selectLeft: 0,/*选择框左边界*/
          selectTop: 0,/*选择框上边界*/
          canvas: '',/*预览头像对象*/
          currentImage: '',/*图片实际htmlElement jq对象*/
          /**
           * canvas 绘画函数
           */
          draw: ()=>{
            let image = this.changeHeadImage;
            let selection = image.select[0];
            let ctx = image.canvas.getContext('2d');
            let xFactor = image.naturalWidth / image.offsetWidth;
            let yFactor = image.naturalHeight / image.offsetHeight;
            let sx = (selection.offsetLeft - image.offsetLeft) * xFactor;
            let sy = (selection.offsetTop - image.offsetTop) * yFactor;
            let sWidth = selection.offsetWidth * xFactor;
            let sHeight = selection.offsetHeight * yFactor;
            let dx = 0;
            let dy = 0;
            let dWidth = image.canvas.offsetWidth * 4;
            let dHeight = image.canvas.offsetHeight * 4;
            ctx.drawImage(image.currentImage[0], sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight);
          }
        },
      }
    },
    components: {
      LineExample,
    },
    methods: {
      openModal(){
        $('.modal').modal('show');
      },
      /**
       * 选择图片函数
       * @param e
       */
      selectHeadImage(e){
        const target = e.target || e.srcElement;
        let reader = new FileReader();
        let image = this.changeHeadImage;
        image.canvas = $('#myca canvas')[0];
        image.currentImage = $('#previewImg');
        reader.onload = function () {
          image.file = this.result;
        };
        reader.addEventListener("loadend", e => {
          const img = image.currentImage;
          image.maxHeight = img.height();
          image.maxWidth = img.width();
          image.maxSize = Math.min(image.maxHeight, image.maxWidth);
          image.offsetWidth = img[0].offsetWidth;
          image.offsetHeight = img[0].offsetHeight;
          image.offsetLeft = img[0].offsetLeft;
          image.offsetTop = img[0].offsetTop;
          image.naturalHeight = img[0].naturalHeight;
          image.naturalWidth = img[0].naturalWidth;
          image.select =img.siblings('div');
          image.select.css({
            top: 0,
            left: 0,
            width:  image.maxSize,
            height: image.maxSize,
            display: 'block',
          });
          image.draw();
          $('#resize').attr({
            max: image.maxSize,
            value: image.maxSize,
          })
        });
        reader.readAsDataURL(target.files[0]);
      },
      /**
       * 设置图片选择框大小
       */
      setSelectSize(e){
        let size = (e.target || e.srcElement).value;
        const image = this.changeHeadImage;
        const selection = $('.select-head-image div')[0];
        let left = selection.offsetLeft, top = selection.offsetTop,
            width = selection.offsetWidth, height = selection.offsetHeight;
        let grow = size - width;
        if(grow > 0 && size <= image.maxSize){
          function setSize(a, b, minSize, maxSize, grow){
            let x = grow;
            if(a > minSize && a - grow/2 >= minSize){
              a -= grow / 2;
              b += grow / 2;
              x -= grow / 2;
              if(b + a + (grow / 2) <= maxSize) {
                b += grow / 2;
                x -= grow / 2;
              }
              else {
                x -= maxSize - a - b;
                b += maxSize - a - b;
                if(x > 0){
                  b += Math.min(x, a - minSize);
                  a -= Math.min(x, a - minSize);
                }
              }
            }
            else{
              x -= a - minSize;
              b += a - minSize;
              a = minSize;
              b += Math.min(x, maxSize - b - minSize);
            }
            return {a: a, b: b};
          }
          let t = setSize(left, width, image.selectLeft, image.selectLeft + image.maxSize, grow);
          width = t.b;
          left = t.a;
          t = setSize(top, height, image.selectTop, image.selectTop + image.maxSize, grow);
          top = t.a;
          height = t.b;
        }
        else if(grow < 0){
          left -= grow/2;
          width += grow;
          if(width <= 6) width = 6;
          top -= grow / 2;
          height += grow;
          if(height <= 6) height = 6;
        }
        image.select.css({
          left: left,
          top: top,
          width: width,
          height: height,
        })
        image.draw();
      },
      /**
       * 设置图片选择框的位置
       */
      setSelectPosition(e){
        let target = $(e.target || e.srcElement);
        let image = this.changeHeadImage;
        let selection = image.select;
        $(document).mouseup(function (e){
          target.off('mousemove');
        });
        target.mousemove(function (e){
          const originalEvent = e.originalEvent;
          let left, top;
          left = selection[0].offsetLeft + originalEvent.movementX;
          top = selection[0].offsetTop + originalEvent.movementY;
          if(left + selection[0].offsetWidth > image.maxWidth) left = image.maxWidth - selection[0].offsetWidth;
          if(left < 0) left = 0;
          if(top + selection[0].offsetHeight > image.maxHeight) top = image.maxHeight - selection[0].offsetHeight;
          if(top < 0) top = 0;
          if(image.maxSize === image.maxWidth){
            image.selectTop += originalEvent.movementY;
            image.selectTop = Math.min(image.selectTop, image.maxHeight - image.maxSize);
            image.selectTop = Math.max(0, image.selectTop);
          }
          if(image.maxHeight === image.maxSize){
            image.selectLeft += originalEvent.movementX;
            image.selectLeft = Math.min(image.selectLeft, image.maxWidth - image.maxSize);
            image.selectLeft = Math.max(image.selectLeft, 0);
          }
          selection.css({
            left: left,
            top: top,
          })
          image.draw();
        })
      },
    }
  }
</script>

<style scoped>
  #userInfo{
    overflow-y: auto;
    overflow-x: hidden;
    max-height: calc(100vh - 60px - 55px);
  }
  .top-ImageBackground-box{
    height: 175px;
    background-image: url("/static/image/background.png");
    background-size: cover;
    background-position:center;
    user-select: none;
  }
  .top-ImageBackground-box>div{
    left: 0;
    bottom: 0;
    height: 65px;
    border-bottom: 1px solid #dadce0;
  }
  .cur-UserImage .UserImage{
    height: 90px;
    width: 90px;
    border-radius: 50%;
    transform: translateY(-20px);
    border: 1px solid #dadce0;
    box-shadow: 0vh 0vh 20px rgba(0, 0, 0, 0.5);;
  }
  .UserImage img{
    width: 75px;
    border-radius: 50%;
  }
  .UserImage-up{
    bottom: 8px;
    background: white;
    border-radius: 5px;
    color: rgba(178, 190, 195,1.0);
    cursor: pointer;
  }
  .mid-content-box h5{
    font-size: 1.125rem;
    color: #273849;
  }
  .UserDs{
    font-size: .85rem;
    width: 100%;
    margin-left: -.5rem;
    background: transparent;
    color: black;
    border-radius: 4px;
    border: 1px solid #dadce0;
  }
  .UserDs::-webkit-input-placeholder, .UserDs:focus::-webkit-input-placeholder{
    font-size: .85rem;
  }
  div:hover>.UserDs{
    cursor: pointer;
    background: rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(127, 140, 141,1.0);
  }
  div:hover>.UserDs:focus, .UserDs:focus{
    cursor: text;
    background: #ecf0f1;
    box-shadow: none;
    outline: none;
  }
  .UserDs-submit-btn{
    position: absolute;
    bottom: 0px;
    right: 7px;
    height: 24px;
    width: 50px;
    border: none;
    border-left: thin solid rgba(127, 140, 141,1.0);
    border-radius: 0 6px 6px 0;
    outline: none;
    background: rgba(120, 224, 143,1.0);
    transition: 0.15s;
    visibility: hidden;
    opacity: 0;
  }
  .UserDs-submit-btn:hover{
    color: white;
  }
  .UserDs:focus+.UserDs-submit-btn{
    visibility: visible;
    opacity: 1;
  }
  aside.user-info-card{
    width: 15rem;
    border:1px solid #dadce0;
    flex-shrink: 0;
    flex-grow: 0;
    height: 13rem;
    flex-grow: 0;
  }
  aside.user-info-card h5{
    font-size: 16px;
    font-weight: 600;
  }
  aside.user-info-card ul li{
    list-style: none;
    margin: .3rem  0;
    line-height: calc(1.5em + .5rem + 2px);
    display: flex;
    align-items: center;
  }
  .user-dynamic{
    flex: 1;
    border:1px solid #dadce0;
    height: 1000px;
  }
  #myca{
    height: 140px;
    width: 100%;
    z-index: 1;
  }
  #myca canvas{
    left: 50%;
    transform: translateX(-50%);
    border-radius: 50%;
    box-shadow:  0vh 0vh 20px rgba(0, 0, 0, 0.5);
    border: 6px solid #fff;
    height: 150px;
    width: 150px;
    position: absolute;
  }
  .select-head-image img{
    max-width: 226px;
    user-select: none;
  }
  .select-head-image div{
    position: absolute;
    border-radius: 0px;
    background: none;
    border: 2px solid #fff;
    cursor: grab;
    display: none;
  }
  .slider-block{
    height: 50px;
    width: 320px;
    padding: 0;
  }
  .slider-block input[type='range']{
    width: 300px;
    -webkit-appearance: none;
    background: transparent;
  }
  .slider-block input[type="range"]:focus {
    outline: none;
  }
  .slider-block input[type="range"]::-webkit-slider-runnable-track {
    height: 2px;
    cursor: pointer;
    background: #95a5a6;
    margin-top: 10px;
  }
  .slider-block input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    height: 30px;
    width: 30px;
    border-radius: 15px;
    background: #fff;
    box-shadow:  0vh 0vh 20px rgba(0, 0, 0, 0.5);
    cursor: pointer;
    margin-top: -13px;
  }
  .slider-block input[type="range"]::-moz-range-track {
    width: 100%;
    height: 2px;
    cursor: pointer;
    background: #95a5a6;
  }
  .slider-block input[type="range"]::-moz-range-thumb {
    height: 30px;
    width: 30px;
    border-radius: 20px;
    background: #fff;
    box-shadow:  0vh 0vh 20px rgba(0, 0, 0, 0.5);
    cursor: pointer;
    -webkit-appearance: none;
    margin-top: -13px;
  }
  .slider-block input[type="range"]::-ms-track {
    width: 100%;
    height: 2px;
    cursor: pointer;
    background: #95a5a6;
  }
  .slider-block input[type="range"]::-ms-thumb {
    height: 30px;
    width: 30px;
    border-radius: 20px;
    background: #fff;
    box-shadow:  0vh 0vh 20px rgba(0, 0, 0, 0.5);
    cursor: pointer;
    -webkit-appearance: none;
    margin-top: 0px;
  }
</style>
