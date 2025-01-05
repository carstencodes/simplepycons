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


class GodaddyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "godaddy"

    @property
    def original_file_name(self) -> "str":
        return "godaddy.svg"

    @property
    def title(self) -> "str":
        return "GoDaddy"

    @property
    def primary_color(self) -> "str":
        return "#1BDBDB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GoDaddy</title>
     <path d="M20.702 2.29c-2.494-1.554-5.778-1.187-8.706.654C9.076
 1.104 5.79.736 3.3 2.29c-3.941 2.463-4.42 8.806-1.07 14.167 2.47
 3.954 6.333 6.269 9.77 6.226 3.439.043 7.301-2.273 9.771-6.226
 3.347-5.361 2.872-11.704-1.069-14.167zM4.042 15.328a12.838 12.838 0
 01-1.546-3.541 10.12 10.12 0 01-.336-3.338c.15-1.98.956-3.524
 2.27-4.345 1.315-.822 3.052-.87
 4.903-.137.281.113.556.24.825.382A15.11 15.11 0 007.5 7.54c-2.035
 3.255-2.655 6.878-1.945 9.765a13.247 13.247 0
 01-1.514-1.98zm17.465-3.541a12.866 12.866 0 01-1.547 3.54 13.25 13.25
 0 01-1.513 1.984c.635-2.589.203-5.76-1.353-8.734a.39.39 0
 00-.563-.153l-4.852 3.032a.397.397 0 00-.126.546l.712 1.139a.395.395
 0 00.547.126l3.145-1.965c.101.306.203.606.28.916.296 1.086.41
 2.214.335 3.337-.15 1.982-.956 3.525-2.27 4.347a4.437 4.437 0
 01-2.25.65h-.101a4.432 4.432 0
 01-2.25-.65c-1.314-.822-2.121-2.365-2.27-4.347-.074-1.123.039-2.251.335-3.337a13.212
 13.212 0 014.05-6.482 10.148 10.148 0 012.849-1.765c1.845-.733
 3.586-.685 4.9.137 1.316.822 2.122 2.365 2.271 4.345a10.146 10.146 0
 01-.33 3.334z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://aboutus.godaddy.net/newsroom/media-re'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://aboutus.godaddy.net/newsroom/media-re'''

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
