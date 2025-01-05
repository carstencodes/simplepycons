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


class PlanetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "planet"

    @property
    def original_file_name(self) -> "str":
        return "planet.svg"

    @property
    def title(self) -> "str":
        return "Planet"

    @property
    def primary_color(self) -> "str":
        return "#009DB1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Planet</title>
     <path d="M12.891 6.582c-1.159 0-2.4.457-3.217 1.633h-.033a1.59
 1.59 0 0 0-1.59-1.59h-.048v10.86a1.792 1.792 0 0 0 1.784
 1.784v-4.703h.034c.343.571 1.29 1.536 3.185 1.536 2.857 0 4.572-2.352
 4.572-4.638.002-2.416-1.616-4.882-4.687-4.882zm-.066 7.975c-1.714
 0-3.07-1.388-3.07-3.217 0-1.666 1.242-3.2 3.023-3.2 1.845 0 3.103
 1.616 3.103 3.233-.001 1.905-1.455 3.184-3.056 3.184zM12.001 24A12 12
 0 1 1 24 12.001 12.013 12.013 0 0 1 12.001 24zm0-22.856a10.861 10.861
 0 1 0 10.861 10.862 10.87 10.87 0 0 0-10.86-10.862z" />
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
