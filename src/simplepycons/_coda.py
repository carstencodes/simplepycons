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


class CodaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "coda"

    @property
    def original_file_name(self) -> "str":
        return "coda.svg"

    @property
    def title(self) -> "str":
        return "Coda"

    @property
    def primary_color(self) -> "str":
        return "#F46A54"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Coda</title>
     <path d="M21.194 0H2.806A2.01 2.01 0 0 0 .8 2v20c0 1.1.903 2
 2.006 2h18.388a2.01 2.01 0 0 0
 2.006-2v-.933c-.033-1.2-.067-3.7-.067-4.834
 0-.633-.468-1.166-1.07-1.166-.668 0-1.103.4-1.437.733-1.003.9-2.508
 1.067-3.812.833-.601-.133-1.17-.3-1.638-.6-1.438-.833-2.374-2.4-2.374-4.066
 0-1.667.936-3.2 2.374-4.067.502-.3 1.07-.467 1.638-.6 1.27-.233
 2.809-.067 3.812.833.367.334.802.734 1.437.734.602 0 1.07-.534
 1.07-1.167 0-1.1.034-3.633.067-4.833V2c0-1.1-.903-2-2.006-2Z" />
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
