$ (function(){
    let filter = $('[data-filter]');
    filter.on('click', function (){
        let cat = $(this).data('filter');
        if(cat == 'all'){
            $('[data-cat]').removeClass('hide');
            $('[data-cat]').addClass('d-flex');
        } else {
             $('[data-cat]').each(function (){
            let worckcat = $(this).data('cat');
            if(worckcat != cat){
                if($(this).hasClass('d-flex')){
                    $(this).removeClass('d-flex');
                }
                $(this).addClass('hide');
            } else {
                if($(this).hasClass('hide')){
                    $(this).removeClass('hide');
                }
                $(this).addClass('d-flex');
            }
        });
        }

    });


});