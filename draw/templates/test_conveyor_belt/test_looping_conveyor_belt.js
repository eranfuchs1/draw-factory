{% extends 'test_conveyor_belt/test.html' %}

{% block js_variables %}
let canvas_container_max_x;
if ("{{implement_conveyor_belt}}" != "True")
{
	canvas_container_max_x = 800;
}
{% endblock js_variables %}

{% block canvas_container_interval %}
if ("{{implement_conveyor_belt}}" != "True")
{
	if (canvas_container_x > canvas_container_max_x)
	{
		canvas_container_x = -600;
	}
}
{% endblock canvas_container_interval %}
