#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
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


class AjvIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ajv"

    @property
    def original_file_name(self) -> "str":
        return "ajv.svg"

    @property
    def title(self) -> "str":
        return "Ajv"

    @property
    def primary_color(self) -> "str":
        return "#23C8D2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ajv</title>
     <path d="M8.705 4.718a980.02 980.02 0 0 1 1.211 3.19l2.962
 7.886c.198.526-.054 1.17-.583 1.366-.311.116-.655.06-.926-.11l-1.454
 1.418c.81.775 1.985 1.034 3.116.614 1.602-.593 2.387-2.416
 1.79-4.008L10.984 4.718zm4.153.013 4.57 11.72 1.924.008L24
 4.783l-2.404-.011-3.193 8.832-3.141-8.861zm-8.309.013L0
 16.421l2.354.01 1.092-2.91 4.112.019 1.08 2.92 2.355.012L6.572
 4.754zm.999 2.592L7.15 11.94l-3.316-.016z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/ajv-validator/ajv/blob/95b
15b683dfb60f63c5129b0426629b968d53af8/docs/.vuepress/public/img/ajv.sv'''

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
