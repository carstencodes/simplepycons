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


class RubyOnRailsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rubyonrails"

    @property
    def original_file_name(self) -> "str":
        return "rubyonrails.svg"

    @property
    def title(self) -> "str":
        return "Ruby on Rails"

    @property
    def primary_color(self) -> "str":
        return "#D30001"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ruby on Rails</title>
     <path d="M.741 19.365h8.36s-1.598-7.291
 3.693-10.243l.134-.066c1.286-.637 4.907-2.431 10.702
 1.854.19-.159.37-.286.37-.286s-5.503-5.492-11.63-4.878c-3.079.275-6.867
 3.079-9.09 6.783C1.058 16.233.741 19.365.741
 19.365Zm8.804-.783a10.682 10.682 0 0
 1-.127-1.333l1.143.412c.063.498.159.963.254
 1.376l-1.27-.455Zm-7.799-4.317L.529 13.82c-.201.455-.423.984-.529
 1.27l1.217.444c.137-.359.36-.878.529-1.269Zm7.831.296.857.677c.042-.413.116-.825.222-1.238l-.762-.603c-.137.391-.233.783-.317
 1.164Zm2.042-2.646-.508-.762c.191-.243.413-.486.656-.709l.476.72a5.958
 5.958 0 0 0-.624.751ZM4.19
 8.878l.752.656c-.254.265-.498.551-.72.836l-.815-.698c.244-.265.508-.529.783-.794Zm9.799
 1.027-.243-.73c.265-.117.571-.233.931-.339l.233.698a6.82 6.82 0 0
 0-.921.371Zm3.122-.656.042-.667c.339.021.688.064
 1.048.138l-.042.656a5.859 5.859 0 0 0-1.048-.127ZM8.942
 6.392l-.476-.731c-.265.138-.54.286-.826.455l.487.741c.275-.169.54-.328.815-.465Zm9.217-.053.042-.709c-.095-.053-.36-.18-1.026-.371l-.043.699c.349.116.688.243
 1.027.381ZM13.238 5.28h.106l-.212-.645c-.328
 0-.666.021-1.016.063l.201.625a8.87 8.87 0 0 1 .921-.043Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/simple-icons/simple-icons/'''

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
