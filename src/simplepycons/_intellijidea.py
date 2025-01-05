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


class IntellijIdeaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "intellijidea"

    @property
    def original_file_name(self) -> "str":
        return "intellijidea.svg"

    @property
    def title(self) -> "str":
        return "IntelliJ IDEA"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>IntelliJ IDEA</title>
     <path d="M0 0v24h24V0zm3.723
 3.111h5v1.834h-1.39v6.277h1.39v1.834h-5v-1.834h1.444V4.945H3.723zm11.055
 0H17v6.5c0 .612-.055 1.111-.222 1.556-.167.444-.39.777-.723
 1.11-.277.279-.666.557-1.11.668a3.933 3.933 0 0 1-1.445.278c-.778
 0-1.444-.167-1.944-.445a4.81 4.81 0 0
 1-1.279-1.056l1.39-1.555c.277.334.555.555.833.722.277.167.611.278.945.278.389
 0 .721-.111 1-.389.221-.278.333-.667.333-1.278zM2.222 19.5h9V21h-9z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
