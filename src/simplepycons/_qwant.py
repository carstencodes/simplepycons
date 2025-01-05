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


class QwantIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qwant"

    @property
    def original_file_name(self) -> "str":
        return "qwant.svg"

    @property
    def title(self) -> "str":
        return "Qwant"

    @property
    def primary_color(self) -> "str":
        return "#282B2F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qwant</title>
     <path d="M9.313 5.163c4.289 0 7.766 2.589 7.766 7.616 0
 4.759-3.072 7.301-7.003 7.59 1.87 1.142 4.693 1.143
 6.45-.348l.547.297-.615
 3.074-.226.285c-3.118.918-5.947-.099-7.921-3.329-3.816-.37-6.765-2.9-6.765-7.568
 0-5.03 3.477-7.617 7.766-7.617zm0 13.88c2.756 0 4.08-2.804 4.08-6.264
 0-3.46-1.148-6.264-4.08-6.264-2.85 0-4.08 2.805-4.08 6.264 0 3.46
 1.182 6.264 4.08 6.264zm8.719-16.319L18.734 0h.263l.703 2.725
 2.754.71v.248l-2.754.71-.703
 2.725h-.263l-.702-2.725-2.696-.695V3.42z" />
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
