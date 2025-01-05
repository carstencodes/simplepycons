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


class AnthropicIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "anthropic"

    @property
    def original_file_name(self) -> "str":
        return "anthropic.svg"

    @property
    def title(self) -> "str":
        return "Anthropic"

    @property
    def primary_color(self) -> "str":
        return "#191919"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Anthropic</title>
     <path d="M17.3041 3.541h-3.6718l6.696 16.918H24Zm-10.6082 0L0
 20.459h3.7442l1.3693-3.5527h7.0052l1.3693 3.5528h3.7442L10.5363
 3.5409Zm-.3712 10.2232 2.2914-5.9456 2.2914 5.9456Z" />
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
