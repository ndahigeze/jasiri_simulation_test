


$(function () {
    $(".phone-rwanda-format").attr("pattern","^[+]*[2][5][0][7][2893][0-9]{7}")
})




 let rwanda_format = document.querySelector(".phone-rwanda-format");
      if(rwanda_format!=null){
         window.intlTelInput(rwanda_format,({
                allowDropdown:true,
                autoHideDialCode:false,
                autoPlaceholder:"",
                customPlaceholder:null,
                dropdownContainer:null,
                excludeCountries: [],
                formatOnDisplay:true,
                geoIpLookup:null,
                hiddenInput:"",
                initialCountry:"",
                localizedCountries:null,
                nationalMode:false,
                onlyCountries: ["rw"],
                placeholderNumberType:"MOBILE",
                preferredCountries: ["rw"],
                separateDialCode:false,
                utilsScript:""
            }));
      }


       let international_format = document.querySelector(".phone-international-format");
           if(international_format!=null){
               window.intlTelInput(international_format,({
                allowDropdown:true,
                autoHideDialCode:false,
                autoPlaceholder:"polite",
                customPlaceholder:null,
                dropdownContainer:null,
                excludeCountries: [],
                formatOnDisplay:true,
                geoIpLookup:null,
                hiddenInput:"",
                initialCountry:"",
                localizedCountries:null,
                nationalMode:false,
                onlyCountries: [],
                placeholderNumberType:"MOBILE",
                preferredCountries: ["rw" ],
                separateDialCode:false,
                utilsScript:""
            }));
           }



