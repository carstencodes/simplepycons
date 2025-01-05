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


class InspireIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "inspire"

    @property
    def original_file_name(self) -> "str":
        return "inspire.svg"

    @property
    def title(self) -> "str":
        return "INSPIRE"

    @property
    def primary_color(self) -> "str":
        return "#00E5FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>INSPIRE</title>
     <path d="M0 0v24h24V0H0zm3.873 3.6875c1.0359-.0008 1.8758.8391
 1.875 1.875-.0003 1.035-.8399 1.8738-1.875 1.873C2.8387 7.4352 2.0003
 6.5968 2 5.5625c-.0008-1.035.838-1.8747
 1.873-1.875zm4.4903.5078h3.5312l6.7344
 10.8125h.045V4.1953H22v16.1172h-3.5469l-6.7168-10.791h-.0468v10.791H8.3633V4.1953zm-6.123
 4.7871s.013.0041 3.3886 0v11.2754H2.2402V8.9824z" />
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
