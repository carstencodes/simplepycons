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


class VagrantIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vagrant"

    @property
    def original_file_name(self) -> "str":
        return "vagrant.svg"

    @property
    def title(self) -> "str":
        return "Vagrant"

    @property
    def primary_color(self) -> "str":
        return "#1868F2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vagrant</title>
     <path d="M3.556 0L.392 1.846V4.11l7.124 17.3L11.998
 24l4.523-2.611 7.083-17.345V1.848l.004-.002L20.44 0l-5.274
 3.087v2.111l-3.168 7.384-3.164-7.384V3.109l-.017-.008.017-.01z" />
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
