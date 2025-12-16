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


class MulesoftIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mulesoft"

    @property
    def original_file_name(self) -> "str":
        return "mulesoft.svg"

    @property
    def title(self) -> "str":
        return "Mulesoft"

    @property
    def primary_color(self) -> "str":
        return "#00A0DF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mulesoft</title>
     <path d="M12 0C5.373 0 0 5.373 0 12c0 6.628 5.373 12 12 12 6.628
 0 12-5.373 12-12S18.627 0 12 0zm0 1.055c6.045 0 10.945 4.9 10.945
 10.945S18.045 22.945 12 22.945 1.055 18.045 1.055 12c0-6.044
 4.9-10.945 10.945-10.945zM7.33 4.364s-2.993 1.647-3.96 5.25c-.647
 2.224-.39 4.702.903 6.914a8.957 8.957 0 0 0 3.95
 3.596l.802-3.062c-1.801-.85-3.11-2.571-3.11-4.79a5.647 5.647 0 0 1
 .943-3.141l3.752 5.866h2.792l3.753-5.866a5.647 5.647 0 0 1 .943
 3.14c0 2.22-1.308 3.94-3.109 4.791l.802 3.062a8.957 8.957 0 0 0
 3.948-3.594c1.294-2.213
 1.551-4.692.904-6.916l.002.003c-.966-3.603-3.96-5.251-3.96-5.251l-.336.527-4.341
 6.797h-.003L7.656 4.876z" />
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
