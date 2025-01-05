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


class ZendeskIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zendesk"

    @property
    def original_file_name(self) -> "str":
        return "zendesk.svg"

    @property
    def title(self) -> "str":
        return "Zendesk"

    @property
    def primary_color(self) -> "str":
        return "#03363D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zendesk</title>
     <path d="M12.914 2.904V16.29L24 2.905H12.914zM0 2.906C0 5.966
 2.483 8.45 5.543 8.45s5.542-2.484 5.543-5.544H0zm11.086 4.807L0
 21.096h11.086V7.713zm7.37 7.84c-3.063 0-5.542 2.48-5.542
 5.543H24c0-3.06-2.48-5.543-5.543-5.543z" />
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
