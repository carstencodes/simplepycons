#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class FlaskIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "flask"

    @property
    def original_file_name(self) -> "str":
        return "flask.svg"

    @property
    def title(self) -> "str":
        return "Flask"

    @property
    def primary_color(self) -> "str":
        return "#3BABC3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Flask</title>
     <path d="M10.773 2.878c-.013 1.434.322 4.624.445 5.734l-8.558
 3.83c-.56-.959-.98-2.304-1.237-3.38l-.06.027c-.205.09-.406.053-.494-.088l-.011-.018-.82-1.506c-.058-.105-.05-.252.024-.392a.78.78
 0 0 1
 .358-.331l9.824-4.207c.146-.064.299-.063.4.004.106.062.127.128.13.327Zm.68
 7c.523 1.97.675 2.412.832 2.818l-7.263 3.7a19.35 19.35 0 0
 1-1.81-2.83l8.24-3.689Zm12.432
 8.786h.003c.283.402-.047.657-.153.698l-.947.37c.037.125.035.319-.217.414l-.736.287c-.229.09-.398-.059-.42-.2l-.025-.125c-4.427
 1.784-7.94
 1.685-10.696.647-1.981-.745-3.576-1.983-4.846-3.379l6.948-3.54c.721
 1.431 1.586 2.454 2.509 3.178 2.086 1.638 4.415 1.712 5.793
 1.563l-.047-.233c-.015-.077.007-.135.086-.165l.734-.288a.302.302 0 0
 1 .342.086l.748-.288a.306.306 0 0 1 .341.086l.583.89Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/pallets/flask/blob/85c5d93'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
