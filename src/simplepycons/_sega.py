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


class SegaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sega"

    @property
    def original_file_name(self) -> "str":
        return "sega.svg"

    @property
    def title(self) -> "str":
        return "Sega"

    @property
    def primary_color(self) -> "str":
        return "#0089CF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sega</title>
     <path d="M21.229 4.14l-.006 3.33h-10.6c-.219 0-.397.181-.397.399
 0 .221.18.399.397.399l2.76-.016c4.346 0 7.868 3.525 7.868 7.869 0
 4.348-3.522 7.869-7.869 7.869L2.748 24l.005-3.375h10.635c2.487 0
 4.504-2.016 4.504-4.504
 0-2.49-2.017-4.506-4.506-4.506l-2.771-.03c-2.06
 0-3.727-1.666-3.727-3.72 0-2.061 1.666-3.726
 3.723-3.726h10.618zM2.763 19.843l-.004-3.331h10.609c.21 0
 .383-.175.383-.387 0-.213-.173-.385-.384-.385h-2.744c-4.345
 0-7.867-3.525-7.867-7.871S6.278 0 10.623 0l10.6.003.006
 3.35-10.604.003c-2.49 0-4.5 2.019-4.5 4.507 0 2.489 2.024 4.504 4.515
 4.504l2.775.03c2.055 0 3.72 1.668 3.72 3.724 0 2.055-1.665 3.719-3.72
 3.719H2.765l-.002.003z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:SEGA_'''

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
