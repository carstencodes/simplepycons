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


class ChakraUiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chakraui"

    @property
    def original_file_name(self) -> "str":
        return "chakraui.svg"

    @property
    def title(self) -> "str":
        return "Chakra UI"

    @property
    def primary_color(self) -> "str":
        return "#1BB2A9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Chakra UI</title>
     <path d="M7.678 1.583a3.492 3.492 0 0 0-3.03 1.76L.265
 10.997a2.035 2.035 0 0 0-.064 1.886l4.486 7.784a3.493 3.493 0 0 0
 3.03 1.751l8.602-.01a3.495 3.495 0 0 0 3.026-1.759l4.39-7.655a2.025
 2.025 0 0 0-.002-2.008L19.339 3.34a3.494 3.494 0 0
 0-3.028-1.756Zm4.365 1.244V9.11c0 .32.226.595.54.656l6.089
 1.187c-2.005 3.466-4.006 6.934-6.008
 10.4-.17.296-.62.176-.62-.166v-6.286a.667.667 0 0
 0-.538-.656l-6.072-1.193 5.988-10.393c.168-.29.621-.178.621.168z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/chakra-ui/chakra-ui/blob/e'''

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
