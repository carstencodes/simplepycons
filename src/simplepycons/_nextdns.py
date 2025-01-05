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


class NextdnsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nextdns"

    @property
    def original_file_name(self) -> "str":
        return "nextdns.svg"

    @property
    def title(self) -> "str":
        return "NextDNS"

    @property
    def primary_color(self) -> "str":
        return "#007BFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NextDNS</title>
     <path d="m22.195
 6.512-.001-.019c-.01-.23-.017-.474-.022-.746a2.543 2.543 0 0
 0-2.395-2.492c-2.759-.154-4.894-1.053-6.717-2.831l-.016-.015a1.536
 1.536 0 0 0-2.087 0l-.016.015C9.117 2.202 6.982 3.101 4.223
 3.256a2.543 2.543 0 0 0-2.395
 2.492c-.004.269-.011.513-.022.745l-.001.044c-.053 2.813-.12 6.315
 1.052 9.494.644 1.748 1.619 3.267 2.899 4.516 1.458 1.422 3.367 2.552
 5.674 3.356.075.026.153.048.233.063a1.668 1.668 0 0 0 .675
 0c.079-.015.158-.037.233-.063 2.305-.806 4.212-1.936 5.668-3.358
 1.28-1.25 2.255-2.769 2.9-4.518 1.176-3.188 1.109-6.696 1.056-9.515Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/simple-icons/simple-icons/'''

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
