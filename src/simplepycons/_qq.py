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


class QqIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qq"

    @property
    def original_file_name(self) -> "str":
        return "qq.svg"

    @property
    def title(self) -> "str":
        return "QQ"

    @property
    def primary_color(self) -> "str":
        return "#1EBAFC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>QQ</title>
     <path d="M21.395 15.035a40 40 0 0
 0-.803-2.264l-1.079-2.695c.001-.032.014-.562.014-.836C19.526 4.632
 17.351 0 12 0S4.474 4.632 4.474 9.241c0 .274.013.804.014.836l-1.08
 2.695a39 39 0 0 0-.802 2.264c-1.021 3.283-.69 4.643-.438 4.673.54.065
 2.103-2.472 2.103-2.472 0 1.469.756 3.387 2.394
 4.771-.612.188-1.363.479-1.845.835-.434.32-.379.646-.301.778.343.578
 5.883.369 7.482.189 1.6.18 7.14.389
 7.483-.189.078-.132.132-.458-.301-.778-.483-.356-1.233-.646-1.846-.836
 1.637-1.384 2.393-3.302 2.393-4.771 0 0 1.563 2.537 2.103
 2.472.251-.03.581-1.39-.438-4.673" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://en.wikipedia.org/wiki/File:Tencent_QQ'''

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
