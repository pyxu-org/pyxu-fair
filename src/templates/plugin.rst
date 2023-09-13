.. _plugins-page:

.. |br| raw:: html

   </br>

.. raw:: html

    <!-- CSS overrides on the pyxu-fair only -->
    <style>

    .summaryinfo {
        color: #000;
        font-size: 80%;
        margin-bottom: 12px;
        margin-top: 12px;
    }

    .entrypointraw {
        color: #777;
    }
    .badge {
        white-space: nowrap;
        display: inline-block;
        vertical-align: middle;
        /*vertical-align: baseline;*/
        font-family: "DejaVu Sans", Verdana, Geneva, sans-serif;
        /*font-size: 90%;*/
    }
    .currentstate {
        color: #666;
        font-size: 90%;
        margin-bottom: 12px;
    }
    span.badge-left {
        border-radius: .25rem;
        border-top-right-radius: 0;
        border-bottom-right-radius: 0;
        color: #212529;
        background-color: #A2CBFF;
        /* color: #ffffff; */
        text-shadow: 1px 1px 1px rgba(0,0,0,0.3);

        padding: .25em .4em;
        line-height: 1;
        text-align: center;
        white-space: nowrap;
        float: left;
        display: block;
    }

    span.badge-right {
        border-radius: .25rem;
        border-top-left-radius: 0;
        border-bottom-left-radius: 0;

        color: #fff;
        background-color: #343a40;

        padding: .25em .4em;
        line-height: 1;
        text-align: center;
        white-space: nowrap;
        float: left;
        display: block;
    }

    .badge-right.light-blue, .badge-left.light-blue {
        background-color: #A2CBFF;
        color: #212529;
    }

    .badge-right.light-red, .badge-left.light-red {
        background-color: rgb(255, 162, 162);
        color: rgb(43, 14, 14);
    }

    .badge-right.red, .badge-left.red {
        background-color: #e41a1c;
        color: #fff;
    }

    .badge-right.blue, .badge-left.blue {
        background-color: #377eb8;
        color: #fff;
    }

    .badge-right.green, .badge-left.green {
        background-color: #4daf4a;
        color: #fff;
    }

    .badge-right.purple, .badge-left.purple {
        background-color: #984ea3;
        color: #fff;
    }

    .badge-right.orange, .badge-left.orange {
        background-color: #ff7f00;
        color: #fff;
    }

    .badge-right.brown, .badge-left.brown {
        background-color: #a65628;
        color: #fff;
    }

    .badge-right.dark-gray, .badge-left.dark-gray {
        color: #fff;
        background-color: #343a40;
    }


    .badge a {
        text-decoration: none;
        padding: 0;
        border: 0;
        color: inherit;
    }

    .badge a:visited, .badge a:active {
        color: inherit;
      }

    .badge a:focus, .badge a:hover {
        color: rgba(255,255,255,0.5);
        mix-blend-mode: difference;
        text-decoration: none;
        /* background-color: rgb(192, 219, 255); */
    }


    .svg-badge {
        vertical-align: middle;
    }

    .tooltiptext {
        visibility: hidden;
        /* width: 120px; */
        background-color: rgb(255, 247, 175);
        color: #000;
        text-align: center;
        border-radius: 6px;
        padding: 5px;

        /* Position the tooltip */
        position: absolute;
        z-index: 1;
    }

    .tooltip:hover .tooltiptext {
        visibility: visible;
    }
    </style>

{{ '*' * (plugin.name | length) }}
{{plugin.name}}
{{ '*' * (plugin.name | length) }}

{%  if plugin.description %}
Description
===========

.. raw:: html
    {{ plugin.description | indent(4) }}
{% endif %}

General information
===================

.. raw:: html

    {%  if plugin.short_description %}
    <p>
        <strong>Short description</strong>: {{ plugin.short_description }}
    </p>
    {% endif %}

    <p class="currentstate">
        {% if dev_status %}
        <img class="svg-badge" src="../../_static/plugins/status/{{ dev_status[1] }}" title="{{ dev_status[0] }}">
        {%- endif -%}
    </p>
    {%  if plugin.pip_install_cmd %}
    <p>
        <strong>How to install</strong>: <code>{{ plugin.pip_install_cmd }}</code>
    </p>
    {% endif %}

    <p>
        <strong>Source code</strong>: <a href="{{ plugin.home_page}}" target="_blank">Go to the source code repository</a>
    </p>

    {% if plugin.docs_url %}
    <p>
        <strong>Documentation</strong>: <a href="{{ plugin.docs_url }}" target="_blank">Go to plugin documentation</a>
    <p>
    {% else %}
    <p>
        <strong>Documentation</strong>: No documentation provided by the package author
    <p>
    {% endif %}


Detailed information
====================

.. raw:: html
    {%  if plugin.author %}
    <p>
        <strong>Author(s)</strong>: {{ plugin.author }}
    </p>
    {% endif %}
    {%  if plugin.author_email %}
    <p>
        <strong>Contact</strong>: <a href="mailto:{{ plugin.author_email }}">{{ plugin.author_email }}</a>
    </p>
    {% endif %}
    {%  if plugin.version %}
    <p>
        <strong>Most recent version</strong>: {{ plugin.version }}
    </p>
    {% endif %}
    {%- if plugin.pyxu_version -%}
    <p>
        <strong>Compatibility</strong>:
        <img class="svg-badge" title="Compatible with Pyxu {{ plugin.pyxu_version }}" src="https://img.shields.io/badge/Pyxu-{{ plugin.pyxu_version }}-007ec6.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAARCAYAAADQWvz5AAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAfFJREFUOI2Vkl9IU1Ecxz933TVdFlHOt9pfg1AcBS0MCSUIIRa2XjLowbegiKAggujFN80gevWhHuzdsH8UpJkQ+JKyheRyW1Qyc2xG3Nrudn896C7Ti237vJ3fOedzvr9zjiIiQgVi6PB9CCMd5a9yHJpase8PsCb7cLlcbItskH/3UrSh27J0uVNkxiky4xR9/ICsvrkr3oNuSWuGpDVDus70ysjwPdmKrSzUHz3EWJinkG2sPAaAucUEK/EYJw77mJ54wfinWUsgG8DU5KRZaNhhulEa8gDs3qnQFw4D0BcOk135SeexkFWkaRqnYxkctwZpbvuCnnRuzCoARM6f4kJ/PwCPx8YIdLSTyWU3iZStl12m8H6Q0sdR5I+Nb4bK9eVuvi4scuhoEID5J0+JJxPVRZUEPF46Lp41x78zWZZeTXMuEmH4/kh9IgBf70kQIfX2A6WCDmCmUqtJypQ3iAitXp9l3mapVEFRFOLJBEW9WJvowbVL/xWq9s3NWForFYuM3rnKcuIzA8EWvO1HmHj+jJ7uHq7cvIG/SWU29YPQrjUcqspAsGU9aS2XLQhzU6+xNzppC3XRvGcvAKu/chWL6iQWjYrf7RG/2yOpVMqs15SokvJXyOfzOBwO8zXrfjWzE8MAIJdbb6/uRNvxD+osJR0a6bPBAAAAAElFTkSuQmCC">
    </p>
    {% endif %}


Components contributed
======================

.. raw:: html
    <p class="summaryinfo">
        {% for summaryinfoelem in summary_info %}
        <span class="badge">
            <span class="badge-left {{summaryinfoelem.colorclass}}">{{summaryinfoelem.text}}</span>
            <span class="badge-right">{{summaryinfoelem.count}}</span>
        </span>
        {% endfor %}
    </p>
    {% if entry_points %}
    {% for entrypointtype, entrypointlist in entry_points.items() %}
    {% if entrypointtype in entrypointtypes.keys() %}
      {{ entrypointtypes[entrypointtype].shortname}} <span class="entrypointraw">({{ entrypointtype }})</span>
    {% else %}
      {{ entrypointtype }}
    {% endif %}
    <ul>
    {% for ep_name, ep_module in entrypointlist.items() %}
    <li><code>{{ ep_name }}</code>
    {% endfor %}
    </ul>
    {% endfor %}
    {% else %}
    <p>No entry points defined for this plugin.</p>
    {% endif %}
