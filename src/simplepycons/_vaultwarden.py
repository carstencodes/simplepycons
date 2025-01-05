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


class VaultwardenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vaultwarden"

    @property
    def original_file_name(self) -> "str":
        return "vaultwarden.svg"

    @property
    def title(self) -> "str":
        return "Vaultwarden"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vaultwarden</title>
     <path
 d="M11.5405.4477c-.143.2381-.3334.5239-.4382.6286-.1715.181-.181.1715-.7334-.3715-.6667-.6666-.7715-.6476-1.086.2096-.1332.3524-.295.6-.4285.6762-.1905.0953-.2856.0667-.7619-.2761-.8001-.562-.9429-.4763-1.0954.619-.038.2763-.1143.4763-.2095.5144-.0762.0286-.4-.0667-.7049-.219-.781-.3716-.8953-.2858-.9048.619
 0
 .3715-.0476.7238-.0952.7715-.0667.0667-.3144.0476-.781-.0666-.9144-.2191-.9716-.162-.7525.7524.1142.4667.1333.7144.0666.781-.0476.0477-.4.0953-.7715.0953-.9143.0095-.9906.1238-.6095.9049.3714.781.2762
 1.0096-.4477 1.1049-1.0669.1523-1.1335.2857-.543
 1.0762.4763.6286.4477.724-.3429 1.0096-.8476.324-.8667.4286-.2
 1.0954.543.5524.5525.562.3715.7334-.1047.1048-.3905.2953-.6286.4382-.5906.3428-.5906.5714
 0
 .9143.2381.143.5239.3333.6286.4381.181.1715.1715.181-.3715.7335-.6667.6667-.6476.7715.2096
 1.0859.3525.1332.6.2951.6762.4285.0953.1905.0667.2857-.2761.762-.562.8-.4763.9428.6191
 1.0953.2762.038.4762.1143.5143.2095.0286.0763-.0666.4-.219.705-.3716.7809-.2858.8953.619.9048.3715
 0
 .724.0476.7715.0951.0667.0667.0476.3144-.0666.7812-.219.9143-.162.9715.7524.7524.4667-.1143.7144-.1334.7811-.0667.0476.0476.0952.4.0952.7715.0095.9144.1239.9906.9049.6096.781-.3715
 1.0096-.2762 1.1049.4476.1524 1.067.2857 1.1335
 1.0762.543.6286-.4763.724-.4477 1.0097.343.3238.8476.419.8667
 1.1049.1903.6666-.6476.6095-.6571 1.1619.2763.343.581.5715.581.9145 0
 .5523-.9334.4952-.924 1.1619-.2763.6859.6764.781.6573
 1.0954-.2.1333-.3523.2952-.6.4286-.6762.1905-.0953.2858-.0667.762.2762.8.562.943.4762
 1.0953-.619.0381-.2763.1143-.4763.2096-.5144.0762-.0286.4.0666.7048.219.781.3715.8954.2857.905-.619
 0-.3715.0474-.724.0951-.7716.0667-.0667.3143-.0476.781.0667.9145.219.9716.162.7525-.7524-.1143-.4668-.1333-.7145-.0667-.7812.0477-.0475.4-.0951.7715-.0951.9144-.0095.9906-.1238.6097-.905-.3715-.7809-.2763-1.0096.4476-1.1048
 1.0667-.1523
 1.1334-.2857.543-1.0762-.4763-.6287-.4478-.724.3428-1.0097.8477-.3238.8668-.419.1905-1.105-.6477-.6666-.6572-.6095.2762-1.1618.2953-.181.4382-.324.4382-.4573
 0-.1334-.143-.2763-.4382-.4571-.9334-.5525-.924-.4954-.2762-1.1621.6763-.6858.6572-.781-.2-1.0953-.3524-.1334-.6001-.2953-.6763-.4287-.0952-.1905-.0667-.2857.2763-.7619.562-.8001.4761-.9429-.6192-1.0954-.2762-.038-.4762-.1143-.5143-.2096-.0286-.0762.0667-.4.219-.7048.3715-.781.2858-.8953-.619-.905-.3715
 0-.7239-.0474-.7716-.0951-.0666-.0666-.0476-.3143.0667-.781.219-.9143.162-.9715-.7524-.7524-.4668.1142-.7144.1333-.781.0666-.0478-.0477-.0953-.4-.0953-.7715-.0095-.9144-.1238-.9906-.905-.6096-.7809.3714-1.0095.2763-1.1047-.4477-.1524-1.0667-.2858-1.1334-1.0763-.543-.6287.4764-.724.4478-1.0096-.3428-.324-.8476-.4287-.8667-1.0954-.2-.5525.543-.562.5525-.7335.3715-.1047-.1048-.2952-.3905-.438-.6286C12.2739.1429
 12.1309 0 11.9976 0c-.1333 0-.2761.1429-.4571.4477zm.9334
 1.9335c.1048.1048.1905.3143.1905.4762 0
 .162-.0857.3715-.1905.4763-.4096.4095-1.143.1048-1.143-.4763
 0-.362.3048-.6667.6667-.6667.162 0 .3715.0857.4763.1905zM11.007
 4.0004c.924.8953 1.0573.8953 1.9812 0l.6858-.6667.6667.1905c.762.2095
 1.9431.7143 1.9431.8382 0 .038-.8953 2.6287-1.9907 5.7434-1.0953
 3.1146-2.0478 5.8386-2.105
 6.0577-.0666.2286-.1524.4096-.1905.4096-.038
 0-.1143-.162-.162-.3524-.057-.2-1-2.9432-2.1049-6.1054-1.1143-3.1622-2.0192-5.772-2.0192-5.791
 0-.1143 2.1145-.9334
 2.5622-.9811.0285-.0095.3524.2857.7333.6572zm-3.3432 9.601c1.3526
 3.7908 2.4288 6.9054 2.4003
 6.934-.0667.0762-1.0763-.219-1.5048-.4477-.343-.1715-.3525-.1905-.4763-1-.0763-.524-.1906-.905-.3049-1.0573-.1904-.2381-.219-.2381-.8667-.1715-1.4287.162-1.3715.181-1.9335-.5714-.6096-.8096-1.181-1.9431-1.4573-2.9051-.162-.5334-.219-1.0668-.2571-2.0954l-.0477-1.3812.8572-.4571c1.1525-.6
 1.181-.7049.5905-1.8764-.4285-.8477-.4285-.8.124-1.6002.1523-.2286.3142-.381.3523-.3334.038.0381
 1.1716 3.1717 2.524 6.9627Zm11.8203-6.2101.2382.4-.3906.7715c-.5905
 1.181-.562 1.2858.581 1.8859l.8478.4476v1.0763c0 1.2478-.1715
 2.2193-.581 3.2575-.3144.7905-.943 1.8383-1.448
 2.4288l-.3237.381-.7524-.1143c-.4096-.0666-.8668-.1142-1.0096-.1142-.4
 0-.6002.3523-.7335
 1.2858l-.1238.8286-.5048.219c-.581.2573-1.2859.4668-1.3526.3906-.038-.038
 4.01-11.5249
 4.8482-13.7728l.0952-.2381.1905.2381c.1048.1238.2953.4096.419.6287zM3.7586
 8.715c.4478.4382.181 1.0954-.4475 1.0954-.4 0-.6478-.2381-.6478-.6286
 0-.6286.6573-.9144
 1.0954-.4668zm17.221-.1332c.2761.1523.3523.2666.3523.5999 0
 .381-.2477.6287-.6381.6287-.6382
 0-.9144-.6477-.4573-1.0954.2572-.2666.4287-.2952.743-.1332zM7.2352
 19.1543c.3429.8191-.8287
 1.3239-1.2097.5144-.1429-.2953-.1429-.343.0095-.5716.3239-.4952.9906-.4666
 1.2.0572zm10.563-.2572c.238.1905.3047.524.1523.8192-.3905.7619-1.524.219-1.1905-.562.1713-.4286.6667-.5524
 1.0382-.2572z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/dani-garcia/vaultwarden/bl
ob/44e9e1a58ed37bf4b352bb499fd3e97adcd3b26b/resources/vaultwarden-icon'''

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
