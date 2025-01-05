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


class ImessageIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "imessage"

    @property
    def original_file_name(self) -> "str":
        return "imessage.svg"

    @property
    def title(self) -> "str":
        return "iMessage"

    @property
    def primary_color(self) -> "str":
        return "#34DA50"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>iMessage</title>
     <path d="M5.285 0A5.273 5.273 0 0 0 0 5.285v13.43A5.273 5.273 0 0
 0 5.285 24h13.43A5.273 5.273 0 0 0 24 18.715V5.285A5.273 5.273 0 0 0
 18.715 0ZM12 4.154a8.809 7.337 0 0 1 8.809 7.338A8.809 7.337 0 0 1 12
 18.828a8.809 7.337 0 0 1-2.492-.303A8.656 7.337 0 0 1 5.93
 19.93a9.929 7.337 0 0 0 1.54-2.155 8.809 7.337 0 0
 1-4.279-6.283A8.809 7.337 0 0 1 12 4.154" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:IMess'''

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
