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


class JavascriptIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "javascript"

    @property
    def original_file_name(self) -> "str":
        return "javascript.svg"

    @property
    def title(self) -> "str":
        return "JavaScript"

    @property
    def primary_color(self) -> "str":
        return "#F7DF1E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JavaScript</title>
     <path d="M0 0h24v24H0V0zm22.034
 18.276c-.175-1.095-.888-2.015-3.003-2.873-.736-.345-1.554-.585-1.797-1.14-.091-.33-.105-.51-.046-.705.15-.646.915-.84
 1.515-.66.39.12.75.42.976.9 1.034-.676 1.034-.676
 1.755-1.125-.27-.42-.404-.601-.586-.78-.63-.705-1.469-1.065-2.834-1.034l-.705.089c-.676.165-1.32.525-1.71
 1.005-1.14 1.291-.811 3.541.569 4.471 1.365 1.02 3.361 1.244 3.616
 2.205.24 1.17-.87 1.545-1.966
 1.41-.811-.18-1.26-.586-1.755-1.336l-1.83 1.051c.21.48.45.689.81
 1.109 1.74 1.756 6.09 1.666
 6.871-1.004.029-.09.24-.705.074-1.65l.046.067zm-8.983-7.245h-2.248c0
 1.938-.009 3.864-.009 5.805 0 1.232.063 2.363-.138
 2.711-.33.689-1.18.601-1.566.48-.396-.196-.597-.466-.83-.855-.063-.105-.11-.196-.127-.196l-1.825
 1.125c.305.63.75 1.172 1.324 1.517.855.51 2.004.675
 3.207.405.783-.226 1.458-.691
 1.811-1.411.51-.93.402-2.07.397-3.346.012-2.054 0-4.109
 0-6.179l.004-.056z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/voodootikigod/logo.js/blob'''

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
