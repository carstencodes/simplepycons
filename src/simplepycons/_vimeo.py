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


class VimeoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vimeo"

    @property
    def original_file_name(self) -> "str":
        return "vimeo.svg"

    @property
    def title(self) -> "str":
        return "Vimeo"

    @property
    def primary_color(self) -> "str":
        return "#1AB7EA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vimeo</title>
     <path d="M23.9765 6.4168c-.105 2.338-1.739 5.5429-4.894
 9.6088-3.2679 4.247-6.0258 6.3699-8.2898 6.3699-1.409
 0-2.578-1.294-3.553-3.881l-1.9179-7.1138c-.719-2.584-1.488-3.878-2.312-3.878-.179
 0-.806.378-1.8809 1.132l-1.129-1.457a315.06 315.06 0
 003.501-3.1279c1.579-1.368 2.765-2.085 3.5539-2.159 1.867-.18 3.016
 1.1 3.447 3.838.465 2.953.789 4.789.971 5.5069.5389 2.45 1.1309 3.674
 1.7759 3.674.502 0 1.256-.796 2.265-2.385 1.004-1.589 1.54-2.797
 1.612-3.628.144-1.371-.395-2.061-1.614-2.061-.574
 0-1.167.121-1.777.391 1.186-3.8679 3.434-5.7568 6.7619-5.6368
 2.4729.06 3.6279 1.664 3.4929 4.7969z" />
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
