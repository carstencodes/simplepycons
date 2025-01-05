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


class PrdotcoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "prdotco"

    @property
    def original_file_name(self) -> "str":
        return "prdotco.svg"

    @property
    def title(self) -> "str":
        return "pr.co"

    @property
    def primary_color(self) -> "str":
        return "#0080FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>pr.co</title>
     <path d="M11.9998 4.67c1.876-.0025 3.7518.7157 5.1832 2.1468
 1.026 1.0238 1.6037 2.1895 1.898 3.2853l1.7906-1.7905c.7157-.7157
 1.8761-.7157 2.5916 0 .7157.7155.7157 1.8758 0 2.5913l-6.2802
 6.2803c-1.4314 1.4314-3.3073 2.1469-5.1832 2.1469-1.8758
 0-3.7517-.7155-5.1831-2.147-.9442-.944-1.5768-2.0815-1.898-3.2848L3.128
 15.6886c-.7154.716-1.8758.716-2.5915 0-.7153-.7154-.7153-1.8758
 0-2.5915 2.092-2.0933 4.1908-4.1889 5.9512-5.9502 1.6938-1.8595
 3.7695-2.4746 5.5121-2.477zm2.5918
 4.7384c-1.4314-1.4312-3.7521-1.4312-5.1834 0-1.4313 1.4312-1.4313
 3.7522 0 5.1834 1.4313 1.4312 3.7518 1.431 5.1831-.0002 1.4313-1.4312
 1.4313-3.752.0003-5.1832z" />
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
