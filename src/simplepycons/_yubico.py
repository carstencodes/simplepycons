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


class YubicoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "yubico"

    @property
    def original_file_name(self) -> "str":
        return "yubico.svg"

    @property
    def title(self) -> "str":
        return "Yubico"

    @property
    def primary_color(self) -> "str":
        return "#84BD00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Yubico</title>
     <path d="m12.356 12.388 2.521-7.138h3.64l-6.135
 15.093H8.539l1.755-4.136L6 5.25h3.717ZM12 0C5.381 0 0 5.381 0
 12s5.381 12 12 12 12-5.381 12-12S18.619 0 12 0Zm0 1.5c5.808 0 10.5
 4.692 10.5 10.5S17.808 22.5 12 22.5 1.5 17.808 1.5 12 6.192 1.5 12
 1.5Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.yubico.com/wp-content/themes/coro'''

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
