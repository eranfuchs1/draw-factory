if ("{{implement_tabular_design}}" == "True")
{
}
let canvas_ids;
let get_canvas_ids;
let make_new_canvas = (canvas_id) => {
    let canvas = document.createElement("canvas");
    canvas.id = `${canvas_id}`;
    canvas.setAttribute("width", 400);
    canvas.setAttribute("height", 300);
    canvas_container = document.createElement("div");
    canvas_container.setAttribute("class", "canvas_container");
    canvas_container.appendChild(canvas);
    return canvas_container;
};
let canvas_generator_by_ids = (canvas_ids) => {
    let page_num = 0;
    page_num = {{page_number}};
    for (let i = page_num * {{canvas_count}}; i < (page_num * {{canvas_count}}) + {{canvas_count}}; i++)
    {
        if (i >= canvas_ids.length)
        {
            break;
        }
        let canvas_id = canvas_ids[i];
        let canvas_container = make_new_canvas(canvas_id);
        document.body.querySelector(".container").appendChild(canvas_container);
        let context = canvas_container.children[0].getContext('2d');
        load_imageData(context, canvas_container.children[0].id);
    }
};
load_imageData = (context, canvas_id) => {
    let xhttp = new XMLHttpRequest();
    xhttp.responseType = 'json';
    xhttp.onreadystatechange = function() {
        if (this.response)
        {
            console.log(this.response);
            let imgData = context.createImageData(400, 300);
            let res_obj;
            if ('canvas_id' in this.response)
            {
                res_obj = this.response['imgdata'];
            }
            else {
                res_obj = this.response;
            }
            let idx = 0;
            while (idx.toString() in res_obj)
            {
                imgData.data[idx] = res_obj[idx.toString()];
                idx ++;
            }
            context.putImageData(imgData, 0, 0);
        }
    };
    xhttp.open("GET", `{% url 'test_api_get' drawing_tool 'False' 'False' %}${canvas_id}/`, true);
    xhttp.send();
};
get_canvas_ids = () => {
    let xhttp = new XMLHttpRequest();
    xhttp.responseType = 'json';
    xhttp.onreadystatechange = function() {
        if (this.response)
        {
            if ('canvas_ids' in this.response)
            {
                canvas_ids = this.response['canvas_ids'];
                canvas_generator_by_ids(canvas_ids);
            }
        };
    };
    xhttp.open("GET", "{% url 'test_api_get_ids_last_tool' %}", true);
    xhttp.send();
};