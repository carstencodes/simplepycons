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


class HaystackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "haystack"

    @property
    def original_file_name(self) -> "str":
        return "haystack.svg"

    @property
    def title(self) -> "str":
        return "Haystack"

    @property
    def primary_color(self) -> "str":
        return "#0EAF9C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Haystack</title>
     <path d="M2.0084 0C.8992 0 0 .8992 0 2.0084v19.9832C0
 23.1006.8992 24 2.0084 24h19.9832C23.1006 24 24 23.1007 24
 21.9916V2.0084C24 .8992 23.1007 0 21.9916 0Zm9.9624 3.84c3.4303 0
 6.2108 2.7626 6.2108 6.1709v6.4875a.2688.2688 0 0
 1-.2697.2681c-1.3425
 0-2.4306-1.0811-2.4306-2.415v-4.3409c0-1.9265-1.572-3.488-3.5105-3.488s-3.424
 1.562-3.424 3.488v1.608a.2633.2633 0 0 0 .259.2681h1.5394a.2693.2693
 0 0 0 .2753-.263V9.9453c0-.7412.6044-1.3414 1.3503-1.3414s1.3502.6002
 1.3502 1.3414V20.029a.2747.2747 0 0 1-.2807.2682c-1.3362
 0-2.4198-1.0766-2.4198-2.4043v-3.2307a.2747.2747 0 0
 0-.2753-.268H8.8114a.2637.2637 0 0 0-.2646.263v1.0789c0 1.3338-1.1746
 2.4152-2.517 2.4152a.2688.2688 0 0 1-.2698-.268v-7.8724c0-3.4083
 2.7805-6.1709 6.2108-6.1709Z" />
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
