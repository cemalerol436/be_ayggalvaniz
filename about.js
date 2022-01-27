

function loadBrands() {
    $.ajax({
        url: "/get-brands",
        async: false,
        success : setBrandOptions
    });

    function setBrandOptions(data) {


        const options = [
        '<option>Choose</option>'
        ];

        data.result.brands.forEach(item=>{

            options.push('<option value="'+item.brand+'">'+item.brand+'</option>')

        });


        document.getElementById("brands-select").innerHTML = options.join('')

        console.log(data)
    }
}
