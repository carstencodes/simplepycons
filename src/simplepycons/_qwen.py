#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class QwenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qwen"

    @property
    def original_file_name(self) -> "str":
        return "qwen.svg"

    @property
    def title(self) -> "str":
        return "QWen"

    @property
    def primary_color(self) -> "str":
        return "#6950EF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>QWen</title>
     <path d="M23.919 14.545 20.817 9.17l1.47-2.544a.56.56 0 0 0
 0-.566l-1.633-2.83a.57.57 0 0 0-.49-.283h-6.207L12.487.402a.57.57 0 0
 0-.49-.284H8.732a.56.56 0 0 0-.49.284L5.139 5.775h-2.94a.56.56 0 0
 0-.49.284L.077 8.887a.56.56 0 0 0 0 .567L3.18 14.83l-1.47
 2.545a.56.56 0 0 0 0 .566l1.634 2.83a.57.57 0 0 0 .49.283h6.205l1.47
 2.545a.57.57 0 0 0 .49.284h3.266a.57.57 0 0 0
 .49-.284l3.104-5.375h2.94a.57.57 0 0 0 .49-.283l1.634-2.828a.55.55 0
 0 0-.004-.568M8.733.686l1.634 2.828-1.634 2.828H21.8L20.164
 9.17H7.425L5.63 6.06Zm1.306 19.801-6.205-.002 1.634-2.83h3.265L2.201
 6.344h3.267q3.182 5.517 6.367 11.032zm10.124-5.66L18.53 12l-6.532
 11.315-1.634-2.83c2.129-3.673 4.25-7.351 6.373-11.028h3.592l3.102
 5.374z" />
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
