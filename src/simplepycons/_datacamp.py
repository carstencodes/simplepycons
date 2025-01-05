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


class DatacampIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "datacamp"

    @property
    def original_file_name(self) -> "str":
        return "datacamp.svg"

    @property
    def title(self) -> "str":
        return "DataCamp"

    @property
    def primary_color(self) -> "str":
        return "#03EF62"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DataCamp</title>
     <path d="M12.946 18.151v-5.239L21.209 8.2 19.2 7.048l-6.254
 3.567V5.36c0-.356-.192-.689-.5-.866L4.922.177a1.434 1.434 0 0
 0-1.455.044 1.438 1.438 0 0 0-.676 1.224v14.777A1.44 1.44 0 0 0 4.92
 17.49l6.032-3.44v4.683a1 1 0 0 0 .504.867l7.73 4.4
 2.01-1.152-8.25-4.697zM10.953 5.938v5.814L4.785 15.27V2.4l6.168
 3.539v-.001z" />
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
