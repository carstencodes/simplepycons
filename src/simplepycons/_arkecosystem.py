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


class ArkEcosystemIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "arkecosystem"

    @property
    def original_file_name(self) -> "str":
        return "arkecosystem.svg"

    @property
    def title(self) -> "str":
        return "ARK Ecosystem"

    @property
    def primary_color(self) -> "str":
        return "#C9292C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ARK Ecosystem</title>
     <path d="M1.8 0C.806 0 0 .805 0 1.8v20.4c0 .995.805 1.8 1.8
 1.8h20.4c.995 0 1.8-.805
 1.8-1.8V1.8c0-.995-.805-1.8-1.8-1.8H1.8zm10.223 4.39l9.29
 15.098-9.29-9.82-9.351 9.82 9.351-15.097zm0 7.583l1.633
 1.691h-3.285l1.652-1.691zM9.31 14.762h5.41l1.496
 1.574H7.813l1.496-1.574z" />
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
