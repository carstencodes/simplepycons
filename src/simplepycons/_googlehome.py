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


class GoogleHomeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlehome"

    @property
    def original_file_name(self) -> "str":
        return "googlehome.svg"

    @property
    def title(self) -> "str":
        return "Google Home"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Home</title>
     <path d="M12 0a1.44 1.44 0 0 0-.947.399L.547 10.762a1.26 1.26 0 0
 0-.342.808v11.138c0 .768.53 1.292 1.311 1.292h20.968c.78 0 1.311-.522
 1.311-1.292V11.57a1.25 1.25 0 0 0-.34-.804L15.68
 3.097h-.001L12.947.4A1.454 1.454 0 0 0 12 0Zm0 6.727 6.552
 6.456v5.65H5.446v-5.65z" />
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
