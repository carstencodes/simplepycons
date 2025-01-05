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


class ZulipIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zulip"

    @property
    def original_file_name(self) -> "str":
        return "zulip.svg"

    @property
    def title(self) -> "str":
        return "Zulip"

    @property
    def primary_color(self) -> "str":
        return "#6492FE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zulip</title>
     <path d="M22.767 3.589c0 1.209-.543 2.283-1.37 2.934l-8.034
 7.174c-.149.128-.343-.078-.235-.25l2.946-5.9c.083-.165-.024-.368-.194-.368H4.452c-1.77
 0-3.219-1.615-3.219-3.59C1.233 1.616 2.682 0 4.452 0h15.096c1.77-.001
 3.219 1.614 3.219 3.589zM4.452 24h15.096c1.77 0 3.219-1.616
 3.219-3.59 0-1.974-1.449-3.59-3.219-3.59H8.12c-.17
 0-.277-.202-.194-.367l2.946-5.9c.108-.172-.086-.378-.235-.25l-8.033
 7.173c-.828.65-1.37 1.725-1.37 2.934 0 1.974 1.448 3.59 3.218 3.59z"
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
        return '''https://github.com/zulip/zulip/blob/df9e40491'''

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
