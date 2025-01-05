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


class IngressIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ingress"

    @property
    def original_file_name(self) -> "str":
        return "ingress.svg"

    @property
    def title(self) -> "str":
        return "Ingress"

    @property
    def primary_color(self) -> "str":
        return "#783CBD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ingress</title>
     <path d="M22.55 6.55v10.9c0 .434-.184.749-.55.95l-9.45
 5.45c-.367.2-.733.2-1.1 0L2
 18.4c-.366-.201-.55-.516-.55-.95V6.55c0-.434.184-.749.55-.95L11.45.15c.367-.2.733-.2
 1.1 0L22 5.6c.366.201.55.516.55.95zM21 17.8l-3.9-2.25.5-.9 3.9
 2.249V6.549l-.05-.048-8.95-5.2v4.5h-1v-4.5l-9
 5.2v10.398l3.9-2.248.5.899L3 17.8l8.95 5.15h.1L21 17.8zM4.55
 7.675c0-.016.016-.025.05-.025h14.8c.033 0 .05.009.05.025v.075l-7.4
 12.799c0 .034-.017.05-.05.05-.034 0-.05-.016-.05-.05L4.55
 7.75v-.075zm6.95 5.076c0-.301-.15-.533-.45-.7L6.9 9.65h-.05v.05l4.6
 7.9c.033 0 .05-.019.05-.051v-4.8zm.9-1.601l4.2-2.45H7.4l.05.051 4.15
 2.399a.701.701 0 00.8 0zM17.15 9.7v-.05h-.05l-4.15
 2.4c-.3.167-.45.417-.45.749v4.8h.1l4.55-7.899z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://niantic.helpshift.com/a/ingress/?s=in'''
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
