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


class ElementorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "elementor"

    @property
    def original_file_name(self) -> "str":
        return "elementor.svg"

    @property
    def title(self) -> "str":
        return "Elementor"

    @property
    def primary_color(self) -> "str":
        return "#92003B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Elementor</title>
     <path d="M12 0C5.372 0 0 5.372 0 12c0 6.626 5.372 12 12
 12s12-5.372 12-12c0-6.626-5.372-12-12-12ZM9 17H7V7H9Zm8
 0H11V15h6Zm0-4H11V11h6Zm0-4H11V7h6Z" />
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
