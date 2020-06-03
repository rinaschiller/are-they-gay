$( document ).ready(function() {
    console.log( "ready!" );
    ajaxGet('/persons')
    .then((persons) => {
      console.log(persons);
    }).catch(apiErrHandler);
});