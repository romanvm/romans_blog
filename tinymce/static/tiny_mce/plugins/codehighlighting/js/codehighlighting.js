var codehighlighting = {

    className : 'my_personnal_code',
    noGutterDefaultCheck : false,
    autolinksDefaultCheck : false,
    noToolbarDefaultCheck : true,

    saveCode : function () {
        var lang = document.getElementById("ProgrammingLanguages").value;

        var code =  codehighlighting.wrapCode(lang);
        // Added .replace(/</g, "&lt;") to correctly escape xml/html
        code += document.getElementById("CodeArea").value.replace(/</g, "&lt;");
        code += "</pre> ";

        if (document.getElementById("CodeArea").value == ''){
            tinyMCEPopup.close();
            return false;
        }

        tinyMCEPopup.execCommand('mceInsertContent', false, code);
        tinyMCEPopup.close();
    },

    wrapCode : function (lang) {
        var options = "";

        if (document.getElementById("nogutter").checked == true)
            options = "gutter: false; ";
               
        if (document.getElementById("autolinks").checked == true)
            options = options + "auto-links: true; ";

        if (document.getElementById("toolbar").checked == true)
            options = options + "toolbar: false; ";

        if( document.getElementById("firstline").value != '')
            options = options + "first-line: "+document.getElementById("firstline").value+";"

        return '<pre class="brush: '+lang+'; '+options+' class-name: \''+codehighlighting.className+'\' " >';
    },

    cancel : function () {
        tinyMCEPopup.close();
        return false;
    },

    checkDefault : function () {
        if(codehighlighting.noGutterDefaultCheck)
            document.getElementById("nogutter").checked = true;
        if(codehighlighting.autolinksDefaultCheck)
            document.getElementById("autolinks").checked = true;
        if(codehighlighting.noToolbarDefaultCheck)
            document.getElementById("toolbar").checked = true;

        // Set the default start line at 1
        document.getElementById("firstline").value = '1';
    }
};