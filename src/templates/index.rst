:html_theme.sidebar_secondary.remove:
:sd_hide_title: true

.. |br| raw:: html

   </br>

.. raw:: html

    <!-- CSS overrides on the pyxu-fair only -->
    <style>
    .globalsummary-box {
        width:95%;
        padding:10px;
        margin: 20px;
        padding-left: 40px;
        padding-right: 40px;
        background-color: rgba(255,255,255,0.19);
        border:1px solid rgba(50,50,50,0.4);
        border-radius:4px;
        -webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.05);
        box-shadow:inset 0 1px 1px rgba(0,0,0,.05);
        line-height: 1.5;
    }
    .summaryinfo {
        color: #000;
        font-size: 80%;
        margin-bottom: 12px;
        margin-top: 12px;
    }
    .submenu-entry {
        width:90%;
        min-height:140px;
        padding:10px;
        margin: 20px;
        padding-left: 40px;
        padding-right: 40px;
        background-color:rgba(245,245,245,.19);
        border:1px solid rgba(227,227,227,.31);
        border-radius:4px;
        -webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.05);
        box-shadow:inset 0 1px 1px rgba(0,0,0,.05);
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

    .tooltip {
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted black;
    }

    .tooltip .tooltiptext {
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

*********
Pyxu FAIR
*********


.. raw:: html

    <h2 style="font-size: 60px; font-weight: bold; display: inline"><span>Pyxu FAIR</span></h2>
    <h3 style="margin-top: 0; font-weight: bold; text-align: left; ">A marketplace for Pyxu-based plugins</h3>
    <p>While Pyxu offers flexibility and portability across various imaging domains, its general-purpose design might
    not cater to the specific needs of certain imaging communities. The <strong>Pyxu FAIR</strong> addresses this by
    offering a platform that allows for the development, sharing, and integration of specialized plugins to enhance the
    framework.
    </p>

    <h3 style="margin-top: 0; font-weight: bold; text-align: left; ">Want to contribute? </h3>

    <p> You can contribute contribute and share new image processing tools based on Pyxu with the <a href="https://github.com/matthieumeo/cookiecutter-pycsou-plugin"><strong>Pyxu cookiecutter</strong></a>. The cookiecutter aids developers by providing a structured template of classes and functions for plugin creation. Developers can then seamlessly introduce new features in line with Pyxu's established principles and structure. Once you have uploaded your package to <a href="https://pypi.org/">PyPi</a>, you can register your plugin package in the Pyxu FAIR by submitting a pull request to the <a href=https://github.com/matthieumeo/pycsou/><strong>Pyxu repository</strong></a>. See the <a href=contribute.html>Contributing to Pyxu-FAIR</a> tutorial for more details.
    </p>



    <h3 style="margin-top: 0; font-weight: bold; text-align: left; ">Catalogue (alphabetical order)</h3>


**Total Registered Plugin Packages: {{ plugins | length }}**

.. raw:: html

   <div class='globalsummary-box'>
        <div style="display: table;">
            {% for summaryentry in summary_info_count %}
            <span class="badge" style="display: table-row; line-height: 2;">
                <span style="display: table-cell; float: none; text-align: right;"><span class="badge-left {{summaryentry.colorclass}}" style="float: none; display: inline; text-align: right; border: none">{{summaryentry.name}}{% if summaryentry.tooltip %}<span class="tooltiptext">{{ summaryentry.tooltip}}</span>{% endif %}</span></span>
                <span style="display: table-cell; float: none; text-align: left;"><span class="badge-right" style="float: none; display: inline; text-align: left; border: none">{{ summaryentry.total_num }} plugin{% if summaryentry.total_num != 1 %}s{% endif %} in {{ summaryentry.num_entries }} package{% if summaryentry.num_entries != 1 %}s{% endif %} </span></span>
            </span>
        {% endfor %}
        </div>
    </div>


.. grid:: 2 2 3 3
    :gutter: 3

    {% for plugin in plugins %}
    .. grid-item-card::

        .. raw:: html

            <h2 style="font-size: 30px;"><a href="plugins/{{ plugin.name }}.html">{{ plugin.name }}</a></h2>

            <p class="currentstate">
                {% if dev_status %}
                <img class="svg-badge" src="../_static/plugins/status/{{ dev_status[plugin.name][1] }}" title="{{ dev_status[plugin.name][0] }}">
                {%- endif -%}
                {%- if plugin.pyxu_version -%}
                    &nbsp;<img class="svg-badge" title="Compatible with Pyxu plugin.pyxu_version }}" src="https://img.shields.io/badge/Pyxu-{{ plugin.pyxu_version }}-007ec6.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAHpAAAB6QHzJ3XIAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAzpJREFUSImtlU1oXFUUx3/nzVemWq1pbQXXIpSaEiPUtiCSTdK4qAhVLFh0VXChKAbSVbCiUFFxoSAB3ZmKH2C0aivigBpR/AJxERS1hGATg9F2JhN999x7XMx7Ly/TaQmZHvhzLoc793e+eCNmxuVsYXT/9vLmwhNRNXqUqpSlGiFVSRQhFWldNAY2DZ7+vtMbUafgWx9/dt/cYt3mFutWFFkwz2jwVsYD3mj55JzmKHzXrA3bSm1oz2UhJ0/Vnvl5dtH29ve/AVAZHyb/sHnDMr96zpshX63UDsx1hEyeqtmeW3cf21TtYX7+XCs5b7nM233u3GaG3ZgHRQlgvlgoUC6VODh8Jw/efw+//n42ybStAgXUEiXn0BnUrA0NABST2I59t/UDcGz8ae69e4Tfzs6yM30oFkLdQwEoCVISpJIoXYCeVjzaWkCqkg7qW0Ciyfdr7+YzuH3vfmYXzlMulSASzEFoBsxoDTlVyPlcJeGCJyz5bFaNz0eujxAOXlws7Np58+rEDEhX3SwREJJWWW7L0p80WzHR8EsUQsA5pd5YXnNpZmaGl2463N7ovOasINNW4SMry5SU+JrSWpT9ZwhcK6+9fdpCCIQQODB4R3bhi+lpAJaW/uHv8xfYtvU6jh45JKzTlj+86wZEz0lFKKoqKSSOHeVyKemKIUBv7xZ6e7fgnM6vFwBw1cgH84CsfDq0L1JVVBV1yntnPskuRVGEmWHJDFTjuUs/eWmrDp75MvJeH1CnuAQ2+c4U3/zwI7v7+hARSEA9PdWBjUAAxMx4buJkMhdP8K3W+RCIm3VEJNPxsUfWPZO8FQFU3Z8h2PbgfQZIt04EQBK/MYsAxh4+skNdq10uNyPnHLFzOOdwsdswJP2s4FR/CsHvCiFkLVNVDOiiiNVKAJ4aPXpLWkG6cS6rSHHOxruGAGisY2sA6nHaatsrL4wfvyKQ5598/EQKWFluZBVpsL82CoDcTFJzzrsQfCmOYywEzIzXJ57d1g3kov94r3pYVfHqUe/p8cVrugFAh0qi5h9TjXA13nsolvtfnThRv+KQRqG3z7t/oeo2v/nyi41uAQDZRzDVoYcea7bHutX/c3lfgmmbsZoAAAAASUVORK5CYII=">
                {%- endif -%}
            </p>

            <ul class="plugin-info">

            {% if plugin.home_page %}
                <li>
                    <a href="{{ plugin.home_page }}" target="_blank">Home page</a>
                </li>
            {% endif %}

            {% if plugin.docs_url %}
                <li>
                    <a href="{{ plugin.docs_url }}" target="_blank">Documentation</a>
                </li>
            {% endif %}

            {% if plugin.score %}
                <li>
                    <a> Score: {{ plugin.score }} % </a>
                </li>
            {% endif %}
            </ul>

            <p class="summaryinfo">
                {% for summaryinfoelem in summary_info[plugin.name] %}
                <span class="badge">
                    <span class="badge-left {{summaryinfoelem.colorclass}}">{{summaryinfoelem.text}}</span>
                    <span class="badge-right">{{summaryinfoelem.count}}</span>
                </span>
                {% endfor %}
            </p>

    {% endfor %}



.. toctree::
   :maxdepth: 2
   :hidden:

   howto
   contribute
   plugins/index