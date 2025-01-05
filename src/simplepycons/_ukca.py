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


class UkcaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ukca"

    @property
    def original_file_name(self) -> "str":
        return "ukca.svg"

    @property
    def title(self) -> "str":
        return "UKCA"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>UKCA</title>
     <path d="M7.138 11.001H3.852C1.728 11.001 0 9.296 0
 7.201V.011h2.498v7.155c0 .737.622 1.336 1.388 1.336h3.218c.766 0
 1.388-.599 1.388-1.336V.011h2.498v7.19c0 2.095-1.728 3.8-3.852 3.8M24
 .011h-3.23l-5.285 4.16V.011h-2.498V11h2.498V6.814l5.284
 4.187h3.217l-6.952-5.508ZM10.99 23.99H3.8c-2.095
 0-3.8-1.761-3.8-3.885v-3.22C0 14.762 1.705 13 3.8
 13h7.19v2.498H3.834c-.737 0-1.336.622-1.336 1.388v3.219c0 .765.6
 1.387 1.336 1.387h7.156zm4.495-4.995v-2.16c0-.738.622-1.337
 1.387-1.337h3.22c.765 0 1.387.6 1.387 1.336v2.16zM20.125
 13H16.84c-2.124 0-3.852 1.705-3.852
 3.8v7.19h2.498v-2.498h5.994v2.497h2.498V16.8c0-2.094-1.728-3.799-3.852-3.799"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.gov.uk/guidance/using-the-ukca-ma'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.gov.uk/guidance/using-the-ukca-ma'''

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
