var Toast = Swal.mixin({
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 3000
  });
  
  function stoast(msg,status){
    Toast.fire({
      icon: status,
      text: msg,
    })
  }
  
  function switalert(icon,title){
    Swal.fire({
      icon: icon,
      title: title,
      timer: 1500,
      showConfirmButton: false,
    })
  }
  