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
    document.querySelector(".container").appendChild(canvas_container);
    $(canvas_container).offset({left:0});
    return canvas;
};
let canvas_generator_by_ids = (canvas_ids) => {
    let page_num = 0;
    if ("{{implement_pages}}" == "True")
    {
        page_num = parseInt("{{page_num}}");
        for (let i = page_num; i < page_num + 10; i++)
        {
            if (i >= canvas_ids.length)
            {
                break;
            }
            let canvas_id = canvas_ids[i];
        }
    }
    else
    {
        for (let canvas_id of canvas_ids)
        {
            let canvas_container = make_new_canvas(canvas_id);
            document.body.appendChild(canvas_container);
        }
    }
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
        }
    };
    xhttp.open("GET", "{% url test_api_get_ids_last_tool %}", true);
    xhttp.send();
};