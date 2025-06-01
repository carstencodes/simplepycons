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


class HedgedocIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hedgedoc"

    @property
    def original_file_name(self) -> "str":
        return "hedgedoc.svg"

    @property
    def title(self) -> "str":
        return "HedgeDoc"

    @property
    def primary_color(self) -> "str":
        return "#B51F08"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HedgeDoc</title>
     <path d="m12.097.227-1.913 1.341L7.93.914 6.6
 2.816l-2.346.142-.586 2.234-2.157.92.23 2.295L.032 9.995l1.015
 2.083L0 14.14l1.679 1.616-.267 2.291 2.141.955.549 2.243 2.344.178
 1.3 1.925 2.965-.836-6.421-6.298a4.548 4.548 0 0
 1-1.491-3.364c0-2.542 2.1-4.601 4.692-4.601 1.406 0 2.668.607 3.527
 1.57l.978.959 1.195-1.173a4.725 4.725 0 0 1 3.3-1.332c2.591 0 4.692
 2.061 4.692 4.603 0 1.4-.702 2.628-1.644 3.497l-6.291 6.178a1.78 1.78
 0 0 0-1.25-.509c-.489 0-.933.195-1.252.51.006.675.563 1.22 1.252
 1.22.66 0 1.2-.502 1.248-1.139l2.822.78 1.33-1.901
 2.348-.142.585-2.234 2.156-.921-.227-2.297 1.705-1.587-1.015-2.081L24
 10.186l-1.68-1.614.266-2.293-2.14-.955-.55-2.243-2.344-.18L16.253.98l-2.265.619ZM9.292
 13.58c-.614 0-1.111.489-1.111 1.091a1.1 1.1 0 0 0 1.111 1.09 1.1 1.1
 0 0 0 1.112-1.09 1.1 1.1 0 0 0-1.112-1.09zm5.423 0a1.1 1.1 0 0 0-1.11
 1.091 1.1 1.1 0 0 0 1.11 1.09c.616 0 1.112-.488 1.112-1.09
 0-.602-.496-1.09-1.112-1.09z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/hedgedoc/hedgedoc-logo/blo
b/ddc01f74e0260340fa7c2a9d59cf4f21d08aa2c4/LOGOTYPE/SVG/HedgeDoc-Logo%'''

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
